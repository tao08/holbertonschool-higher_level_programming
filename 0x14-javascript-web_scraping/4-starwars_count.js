#!/usr/bin/node
const request = require('request');

const URL = 'https://swapi-api.hbtn.io/api/films/';
const ID = 18;
request(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    let ocurrences = 0;
    const data = JSON.parse(body).results;
    data.forEach(item => {
      const characters = item.characters;
      characters.filter(item => {
        if (item.includes(ID)) ocurrences++;
      }); // end filter í´š
    }); // end for each í´š
    console.log(ocurrences);
  } // else end í´š
}); // end request í´š
