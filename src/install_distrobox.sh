#!/usr/bin/env bash

extension="$1"
file_path="$2"

if [[ "$extension" == "deb" ]]; then
    
    distrobox enter --yes ubuntu-toolbox



elif [[ "$extension" == "rpm" ]]; then
    
    distrobox enter --yes fedora-toolbox





else
    echo "Unsupported extension: $extension"
    exit 1
fi