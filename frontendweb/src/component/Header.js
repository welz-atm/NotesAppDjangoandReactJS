import React, {useState} from "react";
import { Box, Heading, Flex } from "@chakra-ui/core";
import LoginPage from '../screen/LoginPage'
import AllPublishedNotes from './AllPublishedNotes';
import NoteDetail from './NoteDetail'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";



// Note: This code could be better, so I'd recommend you to understand how I solved and you could write yours better :)
const Header = props => {
  const [show, setShow] = useState(false);
  const handleToggle = () => setShow(!show);

  return (
    <Router>
    <Flex
      as="nav"
      align="center"
      justify="space-between"
      wrap="wrap"
      padding="1.5rem"
      bg="teal.500"
      color="white"
      {...props}
    >
      <Flex align="center" mr={5}>
        <Heading as="h1" size="lg" letterSpacing={"-.1rem"}>
          <Link to='/'>The Notes</Link>
        </Heading>
      </Flex>

      <Box display={{ base: "block", md: "none" }} onClick={handleToggle}>
        <svg
          fill="white"
          width="12px"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <title>Menu</title>
          <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
        </svg>
      </Box>

      <Box
        display={{ sm: show ? "block" : "none", md: "block" }}
        mt={{ base: 4, md: 0 }}
      >
        <Link to='/loginpage'>Login</Link>
      </Box>

    </Flex>
     <Switch>
      <Route path='/' exact>
         <AllPublishedNotes/>
      </Route>

        <Route path="/loginpage">
         <LoginPage/>
        </Route>

        <Route path="/:note">
         <NoteDetail/>
        </Route>

      </Switch>
    </Router>
  );
};

export default Header;