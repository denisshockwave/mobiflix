import React, { useState } from "react";

import { useAlert } from 'react-alert'

import { http } from 'src/utils';
import './ValidateVoucher.scss';

const ValidateVoucher = ({ setVoucherValidity, skipVoucherVerification }) => {
  const alert = useAlert();
  const [voucher, setVoucher] = useState('');

  const handleVourcherSubmit = () => {
    http
      .get(`/content/items/verify/${voucher}/`)
      .then((resp) => {
        if (resp.data.status === 'WATCH') {
          localStorage.setItem('voucher', voucher);
          return true;
        }

        alert.show(resp.data.message);
        return false;
      })
      .then((validity) => {
        setVoucherValidity(validity);
      })
      .catch((error) => {
        alert.show(error.message);
        console.log(error);
      });
  }

  const handleSkipVerification = () => {
    skipVoucherVerification(true);
  }

  return (
    <div className="movieplayer-voucher">
      <div className="movieplayer-voucher-container">
        <input
          className="movieplayer-voucher-container__input"
          placeholder="Voucher"
          value={voucher}
          onChange={(event) => setVoucher(event.target.value)}
          />
        <div className="movieplayer-voucher-container__buttons">
          <div
            className="movieplayer-voucher-container__submit"
            onClick={handleVourcherSubmit}
          >Submit</div>
          <a
            href="https://account.netpap.co.ke/mobflix/basestation/netdel/"
            target="_blank"
            className="movieplayer-voucher-container__submit">
            Buy a voucher
          </a>
          <div
            className="movieplayer-voucher-container__submit"
            onClick={handleSkipVerification}
          >Skip</div>
        </div>
      </div>
    </div>
  )
};

export default ValidateVoucher;
