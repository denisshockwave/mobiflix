import { Dispatch, SetStateAction } from 'react';

import { ExpandableMenuSection } from "src/components/ApplicationBar/interfaces";

import { IMovie } from "./interfaces";

export const populateGenres = (movies: IMovie[]): IMovie[] => {
  return Array.from(
    new Set(
      flatten(
        movies.map((movie: IMovie) => movie.genre && movie.genre.split(","))
      )
    )
  );
};

const flatten = arr => {
  return arr.reduce((flat, toFlatten) => {
    return flat.concat(
      Array.isArray(toFlatten) ? flatten(toFlatten) : toFlatten
    );
  }, []);
};

interface IHandleSearchOnChangeSpec {
  movies: IMovie[];
  setFilteredMovies: Dispatch<SetStateAction<IMovie[]>>;
  setSearchWord: Dispatch<SetStateAction<string>>;
}

export const handleSearchOnChange = ({ movies, setFilteredMovies, setSearchWord }: IHandleSearchOnChangeSpec) => event => {
  const filteredMovies = movies.filter((movie: IMovie) =>
    movie.name.toLowerCase().startsWith(event.target.value.toLowerCase())
  );

  setFilteredMovies(filteredMovies);
  setSearchWord(event.target.value);
};

interface IHandleFilterSpec {
  movies: IMovie[];
  setFilteredMovies: Dispatch<SetStateAction<IMovie[]>>;
  setSelectedCategory: Dispatch<SetStateAction<string>>;
  setSelectedGenre: Dispatch<SetStateAction<string>>;
}

export const handleFilter = ({
  movies,
  setFilteredMovies,
  setSelectedCategory,
  setSelectedGenre,
}: IHandleFilterSpec) => (
  filterQuery: string,
  index: number,
  type: ExpandableMenuSection
) => event => {
  let filteredMovies: IMovie[] = [];
  switch (type) {
    case ExpandableMenuSection.Categories:
      filteredMovies = movies.filter(
        (movie: IMovie) => movie.category &&
          movie.category.name.toLowerCase() === filterQuery.toLowerCase()
      );

      setSelectedCategory(index.toString());
      break;
    case ExpandableMenuSection.Genres:
      filteredMovies = movies.filter((movie: IMovie) => {
        if (movie.genre) {
          const genres = movie.genre.split(",");
          return genres.filter(
            item => item.toLowerCase() === filterQuery.toLowerCase()
          ).length;
        }

        return false;
      });

      setSelectedGenre(index.toString());
      break;
    default:
      break;
  }

  setFilteredMovies(filteredMovies);
};

export const handleExpandableDrawerSectionChange = (
  setExpandedDrawerSection: Dispatch<SetStateAction<string>>
) => (section: ExpandableMenuSection) => () => {
  setExpandedDrawerSection(section);
};

export function getMovieList(
  filteredMovies: never[],
  movies: IMovie[],
  searching: boolean
): IMovie[] {
  return filteredMovies.length === 0 && !searching ? movies : filteredMovies;
}
