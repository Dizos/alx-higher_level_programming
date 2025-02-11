#!/usr/bin/node

const request = require('request');


const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;


function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}


request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  
  for (let i = 0; i < characters.length; i++) {
    try {
      const name = await getCharacterName(characters[i]);
      console.log(name);
    } catch (error) {
      console.error(`Error getting character: ${error}`);
    }
  }
});
