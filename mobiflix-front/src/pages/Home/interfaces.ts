export interface IHomeProps {
  movies: IMovie[];
  getMovies: () => Promise<any[]>;
  cookies: any;
}

export interface IMovie {
  id: string;
  name: string;
  poster: string;
  description: string;
  time: string;
  genre: string;
  stars: string;
  director: string;
  imdb: string;
  release: string;
  rating: string;
  video_url?: string;
  trailer_url?: string;
  base_url: string;
  category: {
    name: string;
    id: string;
  }
}