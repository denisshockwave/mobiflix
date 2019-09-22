import React, { useState } from 'react';

import { ExpansionPanel, ExpansionPanelDetails, ExpansionPanelSummary, List, ListItem, ListItemText, SwipeableDrawer } from '@material-ui/core';
import AppBar from '@material-ui/core/AppBar';
import IconButton from '@material-ui/core/IconButton';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import MenuIcon from '@material-ui/icons/Menu';

import { ExpandableMenuSection } from './interfaces';

import './ApplicationBar.scss';

const ApplicationBar = ({
  onSearch,
  onFilter,
  searchWord,
  expandedItem,
  handleMenuExpansion,
  selectedGenre,
  selectedCategory,
  categories,
  genre
}) => {
  const [drawerToggle, onToggleDrawer] = useState(false);

  const toggleDrawer = () => {
    onToggleDrawer(!drawerToggle);
  };

  return (
    <AppBar
      position="relative"
      className="app-bar"
      >
        <Toolbar className="app-bar__toolbar">
          <IconButton
            color="inherit"
            aria-label="Open drawer"
            className="app-bar__toolbar-hum"
            onClick={toggleDrawer}
            >
            <MenuIcon fontSize="large"/>
          </IconButton>
          <Typography
            variant="h6"
            color="inherit"
            noWrap={true}
            className="app-bar__toolbar-header"
            >
            MobiFlix
          </Typography>
          <input
            className="app-bar__toolbar-search"
            placeholder="Search"
            value={searchWord}
            onChange={onSearch}
            />
        </Toolbar>
        <SwipeableDrawer
          open={drawerToggle}
          onClose={toggleDrawer}
          onOpen={toggleDrawer}
        >
          <div className="app-bar__drawer">
            <ExpansionPanel
              expanded={
                expandedItem === ExpandableMenuSection.Genres
                || expandedItem === ExpandableMenuSection.None
              }
              onChange={handleMenuExpansion(ExpandableMenuSection.Genres)}
            >
              <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
                <div
                  tabIndex={0}
                  role="button"
                  className="app-bar__drawer-title"
                >Genres</div>
              </ExpansionPanelSummary>
              <ExpansionPanelDetails>
                <List>
                  {genre.map((text, index) => (
                    <ListItem
                      button={true} 
                      key={index}
                      onClick={onFilter(text, index, ExpandableMenuSection.Genres)}
                      selected={selectedGenre === index.toString()}
                      className="app-bar__drawer-item"
                      >
                      <ListItemText
                        primary={
                          <div className="app-bar__drawer-item">{text}</div>
                        }
                      />
                    </ListItem>
                  ))}
                </List>
              </ExpansionPanelDetails>
            </ExpansionPanel>
            <ExpansionPanel
              expanded={
                expandedItem === ExpandableMenuSection.Categories
                || expandedItem === ExpandableMenuSection.None
              }
              onChange={handleMenuExpansion(ExpandableMenuSection.Categories)}
            >
              <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
                <div
                  tabIndex={0}
                  role="button"
                  className="app-bar__drawer-title"
                >Categories</div>
              </ExpansionPanelSummary>
              <ExpansionPanelDetails>
                <List>
                  {categories.map((category, index) => (
                    <ListItem
                      button={true} 
                      key={index}
                      onClick={onFilter(category.name, index, ExpandableMenuSection.Categories)}
                      selected={selectedCategory === index.toString()}
                      >
                      <ListItemText
                        primary={
                          <div className="app-bar__drawer-item">{category.name}</div>
                        }
                      />
                    </ListItem>
                  ))}
                </List>
              </ExpansionPanelDetails>
            </ExpansionPanel>
            <a
              href="https://netpap.co.ke/mobflix/milestone/msafiri"
              target="_blank"
              className="app-bar__drawer-buy">Buy Voucher</a>
          </div>
        </SwipeableDrawer>
      </AppBar>
  )
}

export default ApplicationBar;
