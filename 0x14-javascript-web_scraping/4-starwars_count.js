#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const moviesWithWedge = films.filter(film =>
      film.characters.some(character => character.endsWith(`/${characterId}/`))
    );
    console.log(moviesWithWedge.length);
  }
});
