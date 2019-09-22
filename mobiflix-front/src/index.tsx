import * as React from 'react';

import * as ReactDOM from 'react-dom';
import {
  HashRouter as Router,
  Route,
} from 'react-router-dom';
import { Provider as AlertProvider } from 'react-alert'
import AlertTemplate from 'react-alert-template-basic'

import Home from './pages/Home';
import Player from './pages/Player';
import registerServiceWorker from './registerServiceWorker';

import './index.scss';

const options = {
  position: 'bottom center',
  timeout: 5000,
  offset: '30px',
  transition: 'scale'
}

ReactDOM.render(
  <AlertProvider template={AlertTemplate} {...options}>
    <div className="app">
      <Router>
        <>
          <Route exact={true} path="/" component={Home} />
          <Route path="/watch/:id" component={Player} />
        </>
      </Router>
    </div>
  </AlertProvider>,
  document.getElementById('root') as HTMLElement
);
registerServiceWorker();
