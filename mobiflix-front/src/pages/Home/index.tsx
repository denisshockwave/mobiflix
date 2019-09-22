import React, { useEffect, useState } from "react";

import { Grid } from "@material-ui/core";

import AppBar from "src/components/ApplicationBar";
import { ExpandableMenuSection } from "src/components/ApplicationBar/interfaces";
import { http } from "src/utils";

import MovieItem from "../../components/MovieItem/index";
import {
  getMovieList,
  handleExpandableDrawerSectionChange,
  handleFilter,
  handleSearchOnChange,
  populateGenres
} from "./utils";

import "./Home.scss";

const Home = () => {
  
  // const [isLoading, toggleLoading] = useState(false);
  const [filteredMovies, setFilteredMovies] = useState([]);
  const [genre, setGenre] = useState([]);
  const [movies, setMovies] = useState([]);
  const [categories, setCategories] = useState([]);
  const [searchWord, setSearchWord] = useState("");
  const [selectedGenre, setSelectedGenre] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("");
  const [expectedDrawerSection, setExpectedDrawerSection] = useState(
    ExpandableMenuSection.None
  );

  useEffect(() => {
    const fetchMovies = () => {
      http
        .get("content/all/")
        .then(resp => {
          return resp.data;
        })
        .then(moviesData => {
          setMovies(moviesData);
          setGenre(populateGenres(moviesData) as any);
        })
        .catch(error => {
          // tslint:disable-next-line: no-console
          console.log("error", error.message);
        });
    };

    fetchMovies();
  }, []);

  useEffect(() => {
    const fetchMovies = () => {
      http
        .get(`/admin/category/list/`)
        .then(resp => {
          return resp.data;
        })
        .then(categoriesData => {
          setCategories(categoriesData);
        })
        .catch(error => {
          // tslint:disable-next-line: no-console
          console.log("error", error.message);
        });
    };

    fetchMovies();
  }, []);

  const movieList = getMovieList(filteredMovies, movies, false);

  return (
    <div className="movie-list">
      <AppBar
        onSearch={handleSearchOnChange({
          movies,
          setFilteredMovies,
          setSearchWord
        })}
        onFilter={handleFilter({
          movies,
          setFilteredMovies,
          setSelectedCategory,
          setSelectedGenre,
        })}
        searchWord={searchWord}
        expandedItem={expectedDrawerSection}
        handleMenuExpansion={handleExpandableDrawerSectionChange(
          setExpectedDrawerSection
        )}
        selectedGenre={selectedGenre}
        selectedCategory={selectedCategory}
        categories={categories}
        genre={genre}
      />
      <>
        {
          movieList.length === 0
            ? (
                <div className="nomovies">No movies found...</div>
              ) 
            : (
                <Grid container={true} className="movielist" spacing={0} wrap="wrap">
                  {
                    movieList.map((data, index) => (
                      <MovieItem {...data} key={new Date().toISOString() + index} />
                    ))
                  }
                </Grid>
              )
        }
      </>
    </div>
  );
};

export default Home;
