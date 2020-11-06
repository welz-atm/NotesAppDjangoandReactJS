import React, {useState, useEffect} from 'react'
import axios from 'axios'
import { Flex, Text, Link, Avatar, Heading, Box} from '@chakra-ui/core'
import { Link as ReachLink, Stack } from "react-router-dom";
import Error from './Error.js'
import Loading from './Loading.js'


export default function AllUsers() {
	const [data, setData] = useState([])
	const [isError, setIsError] = useState(false)
	const [isLoading, setIsLoading] = useState(false)

	useEffect(() => {
		const allUsers = async() => {
			setIsError(false)
			setIsLoading(true)
			try {
				const result = await axios.get('http://localhost:8000/api/user/list/')
				setData(result.data)
			}catch(error){	
				setIsError(true)
			}
			
			setIsLoading(false)
		}
		allUsers()

	}, [])

const noData = !data

return(
    <Flex 
    justify='center'
        align='center'
        flexWrap='wrap'
        flexDirection={noData ? 'column' : 'row'}
        margin='16px'
        padding='16px'>

        {isLoading && !isError ? (<Loading/>) : isError ? <Error/> : (
          data.map((user, index) => 
            <Link as={ReachLink} to='/noteDetail'>
              <Stack isInline spacing={8} align="center">
      				<Box p={5} shadow="md" borderWidth="1px" flex="1" rounded="md" >
      					<Avatar size="2xl" name={user.first} />
      					<Heading fontSize="xl">{user.display_name}</Heading>
      					<Text mt={4}>{user.first} {user.last_name}</Text>
    				</Box>
    			</Stack>
            </Link>))}
      
    </Flex>
	  
		)
}

