#!/usr/bin/node

'use strict';

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    const printCharacter = (index) => {
      if (index === charactersUrls.length) {
        return; // End of characters list
      }

      request.get(charactersUrls[index], (err, res, characterBody) => {
        if (err) {
          console.error(err);
        } else {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
          printCharacter(index + 1); // Print next character
        }
      });
    };

    printCharacter(0); // Start printing characters from index 0
  }
});
