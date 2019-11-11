import { IMovie } from "src/pages/Home/interfaces";

export type IMovieDetails = IMovie & {
  base_url: string;
  expiry_date: string;
  status: Status;
}

export enum Status {
  Watch = 'WATCH'
}
