#!/bin/bash -xe


if [ -f tmp/server.pid ]; then
    # TODO: Возможно, следует использовать другой сигнал
    kill -USR1 $(cat tmp/server.pid)
    rm -f tmp/server.pid
fi
