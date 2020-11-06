import React, {useState, useRef} from 'react';
import { useForm } from 'react-hook-form';
import Error from './Error';
import Loading from './Loading';
import composeRefs from '@seznam/compose-react-refs'
import axios from 'axios';
import {
  Button,
  FormLabel,
  FormControl,
  Text,
  Heading,
  Flex,
  Box,
  Input,} from '@chakra-ui/core';


export default function Login(){
	const [email, setEmail] = useState()
  const [password, setPassword] = useState()
	const [isLoggedIn, setLoggedIn] = useState(false)
	const [isError, setIsError] = useState(false)
	const [isLoading, setIsLoading] = useState(false)
	const initialRef = useRef()
	const {handleSubmit, register} = useForm()
	

	const onSubmit = event => {
		const login = async () => {
			setIsError(false)
			setIsLoading(true)
		    try{
		    	const result = axios.post('http://localhost:8000/user/login/',{email}, {password})
		    	setLoggedIn(true)
          console.log(result.data)
		    }catch(error){
		    	setIsError(true)
		    	setLoggedIn(false)
          		setEmail('')
          		setPassword('')
		    }
			setIsLoading(false)
		}

		login({email}, {password})
	}
	

	return(
    <>
			 <Flex width="full" align="center" justifyContent="center">
      <Box
        p={8}
        maxWidth="500px"
        borderWidth={1}
        borderRadius={8}
        boxShadow="lg"
      >
        {isLoggedIn ? (
          <Box textAlign="center">
            <Text>{email} logged in!</Text>
            <Button
              variantColor="orange"
              variant="outline"
              width="full"
              mt={4}
              onClick={() => setLoggedIn(false)}
            >
              Sign out
            </Button>
          </Box>
        ) : (
          <>
            <Box textAlign="center">
              <Heading>Login</Heading>
            </Box>
            <Box my={4} textAlign="left">
              <form onSubmit={handleSubmit(onSubmit)}>
                {isError && <Error/>}
                <FormControl isRequired>
                  <FormLabel>Email</FormLabel>
                  <Input
                    type="email"
                    name='email'
                    placeholder="test@test.com"
                    size="lg"
                    variant= 'outline'
                    ref= {composeRefs(initialRef, register)}
                  />
                </FormControl>
                <FormControl isRequired mt={6}>
                  <FormLabel>Password</FormLabel>
                  
                    <Input
                    pr="4.5rem"
                    type="password"
                    name='password'
                    placeholder="Enter password"
                    variant='outline'
                    ref={register}
                />
                </FormControl>
                <Button
                  variantColor="teal"
                  variant="outline"
                  type="submit"
                  width="full"
                  mt={4}
                >
                  {isLoading ? (
                    <Loading/>
                  ) : (
                    'Sign In'
                  )}
                </Button>
              </form>
            </Box>
          </>
        )}
      </Box>
    </Flex>
    </>
			)
}