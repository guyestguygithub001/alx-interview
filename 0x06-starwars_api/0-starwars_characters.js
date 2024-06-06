#!/usr/bin/node
const request = require('request');
const SWAPI_API = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const movieUrl = `${SWAPI_API}/films/${movieId}/`;

  request(movieUrl, (error, _, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const characterUrls = JSON.parse(body).characters;
    const characterPromises = characterUrls.map(url =>
      new Promise((resolve, reject) => {
        request(url, (err, __, characterBody) => {
          if (err) {
            reject(err);
            return;
          }
          const characterName = JSON.parse(characterBody).name;
          resolve(characterName);
        });
      })
    );

    Promise.all(characterPromises)
      .then(names => names.forEach(name => console.log(name)))
      .catch(err => console.error(err));
  });
}
