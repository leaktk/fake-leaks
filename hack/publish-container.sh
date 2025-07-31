#!/usr/bin/env bash
set -euo pipefail

version="$1"

semver="${version#v}"
major="v${semver%%.*}"
minor="${semver#*.}"
minor="$major.${minor%%.*}"

podman manifest create "fake-leaks:${version}"
podman manifest create "fake-leaks:${major}"
podman manifest create "fake-leaks:${minor}"

for arch in aarch64 amd64
do
  podman build "--arch=${arch}" -t "quay.io/leaktk/fake-leaks:${version}-${arch}" .
  podman push --format v2s2 "quay.io/leaktk/fake-leaks:${version}-${arch}"
  podman pull "quay.io/leaktk/fake-leaks:${version}-${arch}"
  podman manifest add "fake-leaks:${version}" "quay.io/leaktk/fake-leaks:${version}-${arch}"
  podman manifest add "fake-leaks:${major}" "quay.io/leaktk/fake-leaks:${version}-${arch}"
  podman manifest add "fake-leaks:${minor}" "quay.io/leaktk/fake-leaks:${version}-${arch}"
done

podman manifest push   "fake-leaks:${version}" "docker://quay.io/leaktk/fake-leaks:${version}"
podman manifest push   "fake-leaks:${major}" "docker://quay.io/leaktk/fake-leaks:${major}"
podman manifest push   "fake-leaks:${minor}" "docker://quay.io/leaktk/fake-leaks:${minor}"
