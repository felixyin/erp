#!/usr/bin/env bash
# 覆盖本地的方式，检出代码
git fetch --all
git reset --hard origin/master
git pull