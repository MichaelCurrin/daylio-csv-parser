# Container

This is useful for checking compatibility.

Note that full functionality is not available - just a fixed command in `Dockerfile`.


## Run

Build and run the app using Docker.

```sh
$ make container
```

This uses a _volume_, so when the app in the container writes out, that is available immediately on the host.
