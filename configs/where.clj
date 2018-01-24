; -*- mode: clojure; -*-

(logging/init {:file "riemann_where.log"})

(let [host "127.0.0.1"]
  (tcp-server {:host host})
  (udp-server {:host host})
  (ws-server  {:host host}))

(periodically-expire 300)

(streams
