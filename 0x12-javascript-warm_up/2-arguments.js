#!/usr/bin/node

const process = require('process');
let i = process.argv.length;

if (i > 3)
	console.log('Arguments found');
else if (i == 2)
	console.log('No argument');
else if (i == 3)
	console.log('Argument found');
