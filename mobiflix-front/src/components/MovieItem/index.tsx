import React from 'react';

import { Grid, IconButton, Typography } from "@material-ui/core";
import PlayIcon from '@material-ui/icons/PlayCircleOutlineRounded';
import { Link } from "react-router-dom";

import './MovieItem.scss';

const MovieItem = ({ name, id, poster }) => {
  const addDefaultSrc = (ev) => {
    ev.target.src = 'https://res.cloudinary.com/mikekrantz/image/upload/v1555356246/lloyd-dirks-74271-unsplash.jpg'
  }

  return (
    <Grid
      item={true}
      lg='auto'
      md='auto'
      sm='auto'
      className="movielist-item"
    >
      <Link to={`watch/${id}`}
        className="movielist-item__container">
        <IconButton
          color="inherit"
          aria-label="Open drawer"
          className="movielist-item__container-play"
          >
            <PlayIcon
              fontSize="large"
            />
        </IconButton>
        <Typography
          variant="subtitle1"
          color="textSecondary"
          className="movielist-item__container-title"
          gutterBottom={true}>
          {name}
        </Typography>
      </Link>
      <img
        src={`http://127.0.0.1:8000${poster}`}
        onError={addDefaultSrc}
        className="movielist-item__image"
      />
    </Grid>
  );
}

export default MovieItem;
