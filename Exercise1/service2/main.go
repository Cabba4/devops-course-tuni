package main

import (
    "fmt"
    "net/http"
    "os"
    "os/exec"
    "time"
    "bytes"
)

const (
    storageURL = "http://storage:8200/log" // URL of Storage container
    vStorage   = "/vstorage"  // mounted volume file
)

func getUptime() string {
    out, err := exec.Command("awk", "{printf \"%.3f\", $1/3600}", "/proc/uptime").Output()
    if err != nil {
        return "uptime error"
    }
    return string(out)
}

func getFreeDisk() string {
    out, err := exec.Command("df", "-m", "/").Output()
    if err != nil {
        return "disk error"
    }
    lines := bytes.Split(out, []byte("\n"))
    if len(lines) < 2 {
        return "disk error"
    }
    fields := bytes.Fields(lines[1])
    if len(fields) < 4 {
        return "disk error"
    }
    return string(fields[3]) // 4th column is available space
}

func statusHandler(w http.ResponseWriter, r *http.Request) {
    timestamp := time.Now().UTC().Format(time.RFC3339)
    uptime := getUptime()
    disk := getFreeDisk()
    record := fmt.Sprintf("%s: uptime %s hours, free disk in root: %s MBytes", timestamp, uptime, disk)

    // Send to Storage
    http.Post(storageURL, "text/plain", bytes.NewBufferString(record+"\n"))

    // Append to vStorage
    f, _ := os.OpenFile(vStorage, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
    f.WriteString(record + "\n")
    f.Close()

    // Respond to Service1
    w.Header().Set("Content-Type", "text/plain")
    w.Write([]byte(record))
}

func main() {
    http.HandleFunc("/status", statusHandler)
    fmt.Println("Service2 running on :8201")
    http.ListenAndServe(":8201", nil)
}
