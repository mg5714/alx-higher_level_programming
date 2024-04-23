#!/usr/bin/node

'use strict';

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18'; // ID for Wedge Antilles

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;
    const filmsWithWedge = filmsData.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(filmsWithWedge.length);
  }
});
