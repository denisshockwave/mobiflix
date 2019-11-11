import React, { useEffect, useState } from 'react';

import MoviePlayer from 'src/components/MoviePlayer';
import ValidateVoucher from 'src/components/ValidateVoucher';
import { http } from 'src/utils';

const Player = ({ match }) => {
  const voucherPath = 'voucher';

  const [isVoucherValid, setVoucherValidity] = useState(false);
  const [isVerificationSkipped, skipVoucherVerification] = useState(false);
  const [movieDetails, setMovieDetails] = useState({});

  useEffect(() => {
    const voucher = localStorage.getItem(voucherPath);

    http
      .get(`/content/items/verify/${voucher}/`)
      .then((resp) => {
        if (resp.data.status === 'WATCH') {
          return true
        }
        return false;
      })
      .then((validity) => {
        setVoucherValidity(validity);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  useEffect(() => {
    const voucher = localStorage.getItem(voucherPath);

    http
      .get(`/content/item/${match.params.id}/${voucher}/`)
      .then((resp) => {
        return resp.data.response;
      })
      .then((movieDetailsData) => {
        setMovieDetails(movieDetailsData);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return isVoucherValid || isVerificationSkipped
    ? <MoviePlayer
        movieDetails = {movieDetails}
        verificationSkipped={isVerificationSkipped}
      />
    : <ValidateVoucher
        skipVoucherVerification={skipVoucherVerification}
        setVoucherValidity={setVoucherValidity}
      />
}

export default Player;
