#!/usr/bin/env node

const axios = require('axios');

const baseURL = 'https://swapi.dev/api';

async function getCharactersForMovie(movieId) {
  try {
    const movieResponse = await axios.get(`${baseURL}/films/${movieId}`);

    const movieData = movieResponse.data;

    const characterURLs = movieData.characters;

    for (const characterURL of characterURLs) {
      const characterResponse = await axios.get(characterURL);
      const characterData = characterResponse.data;
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
} else {
  const movieId = process.argv[2];
  getCharactersForMovie(movieId);
}
