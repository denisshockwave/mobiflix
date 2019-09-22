import React from "react";

import IconButton from '@material-ui/core/IconButton';
import BackIcon from '@material-ui/icons/ArrowBackRounded';
import { useAlert } from 'react-alert'
import { Link } from "react-router-dom";
import { BigPlayButton, Player } from 'video-react';

import { http } from "src/utils";

import './MoviePlayer.scss';

const MoviePlayer = ({ movieDetails, verificationSkipped }) => {
  const alert = useAlert();

  const handleClick = async () => {
    const voucher = localStorage.getItem('voucher');
    const status = await http
      .post('/content/item/download/', { voucher })
      .then((response) => {
        return response.data.status;
      })
      .catch(err => {
        console.log(err);
      });

    if (status === 'success') {
      await http
        .get(`${movieDetails!.video_url}`, {
          responseType: 'blob',
          timeout: 3000
        })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', `${movieDetails.name}.mp4`);
          document.body.appendChild(link);
          link.click();
        })
    }

    alert.show('voucher download limit has been reached');
  }

  return (
    <>
      <div className="movieplayer">
        <Link
          to="/"
          className="movieplayer-back">
          <IconButton
            color="inherit"
            aria-label="back"
            >
            <BackIcon fontSize="large"/>
          </IconButton>
        </Link>
        
        <Player
          playsInline={true}
          src={
            verificationSkipped
              ? `${'http://127.0.0.1:8000'}${movieDetails!.trailer_url}`
              : `${'http://127.0.0.1:8000'}${movieDetails!.video_url}`
          }
          className="movieplayer-player"
          fluid={false}
          height={250}
          poster={`${movieDetails!.base_url || 'http://127.0.0.1:8000'}${movieDetails!.poster}`}
        >
          <BigPlayButton position="center" />
        </Player>
        
        <div className="movieplayer-info">
          <div className="movieplayer-info__release">
            {
              new Date(movieDetails.release || '9/17/2016').toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
              })
            }
          </div>
          <div className="movieplayer-info__name">{ movieDetails!.name }</div>
          <div className="movieplayer-info__seperator" />
          <div className="movieplayer-info__description">{ movieDetails!.description }</div>
          <div className="movieplayer-info__actors">Stars: { movieDetails!.stars }</div>
          <div className="movieplayer-info__actors">Genre: { movieDetails!.genre }</div>
          <div className="movieplayer-info__download" onClick={handleClick}>Download</div>
        </div>
      </div>
    </>
  )
}

export default MoviePlayer;