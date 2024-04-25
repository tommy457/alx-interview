#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(URL, async (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const characters = data.characters;

    for (const character of characters) {
      const promise = new Promise((resolve, reject) => {
        request(character, (error, response, names) => {
          if (!error) {
            resolve(JSON.parse(names).name);
          } else {
            reject(error);
          }
        });
      });
      console.log(await promise);
    }
  }
});
