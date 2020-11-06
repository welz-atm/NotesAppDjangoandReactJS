import React from 'react';
import { ThemeProvider, CSSReset,theme } from '@chakra-ui/core';
import Header from './component/Header';


export default function App() {

    return (
    <>  
      <ThemeProvider theme={ theme }>
        <CSSReset/>
        <Header/>
      </ThemeProvider>
    </>
    );
}