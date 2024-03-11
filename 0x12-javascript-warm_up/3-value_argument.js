#!/usr/bin/node
// hi print it please

const args = process.argv[2];

if (args === undefined) {
	console.log("No argument");
} else {
	console.log(args);
}
