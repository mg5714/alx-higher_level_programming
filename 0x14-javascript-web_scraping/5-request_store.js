#!/usr/bin/node

'use strict';

const fs = require('fs');
const request = require('request');

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
