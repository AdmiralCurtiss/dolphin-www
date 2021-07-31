# Copyright (c) 2018 Dolphin Emulator Website Contributors
# SPDX-License-Identifier: MIT

from django import template

register = template.Library()

@register.filter
def artifact_sort(artifacts):
    """Sorts an iterable of artifacts by target system."""
    matchers = (
        ('Windows', 0x8000),
        ('macOS', 0x4000),
        ('Mac OS X', 0x3ff0), # for historical builds
        ('Android', 0x2000),
        ('Ubuntu', 0x1000),
        ('x64', 0x8),
        ('x86', 0x4),
        ('Universal', 0x2),
    )
    def key(artifact):
        k = 0
        for (match, val) in matchers:
            if match in artifact.target_system:
                k += val
        return k
    return sorted(artifacts, key=key, reverse=True)
