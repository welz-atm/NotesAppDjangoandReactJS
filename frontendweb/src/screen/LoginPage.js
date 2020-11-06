import React from 'react';
import  Login from '../component/Login'
import { Flex } from '@chakra-ui/core'


export default function LoginPage(){
	return(
		<>
			<Flex width="full" align="center" justifyContent="center" pt={120}>
      			<Login/>
      		</Flex>
			
		</>
			)
}