#!/usr/bin/env bash
set -euo pipefail

version="$1"

podman manifest create "fake-leaks:${version}"

for arch in aarch64 amd64
do
  podman build "--arch=${arch}" -t "quay.io/leaktk/fake-leaks:${version}-${arch}" .
  podman push --format v2s2 "quay.io/leaktk/fake-leaks:${version}-${arch}"
  podman pull "quay.io/leaktk/fake-leaks:${version}-${arch}"
  podman manifest add "fake-leaks:${version}" "quay.io/leaktk/fake-leaks:${version}-${arch}"
done

podman manifest push   "fake-leaks:${version}" "docker://quay.io/leaktk/fake-leaks:${version}"
