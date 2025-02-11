#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  const getCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  };

  Promise.all(characters.map(url => getCharacterName(url)))
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => console.error(error));
});
