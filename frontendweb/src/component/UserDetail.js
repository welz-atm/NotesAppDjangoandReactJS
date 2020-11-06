import React, {useState, useEffect} from 'react'
import { Box, Flex, Avatar } from "@chakra-ui/core";
import axios from 'axios'
import Error from './Error'
import {useParams} from 'react-router-dom'


export default function UserDetail() {
	const [data, setData] = useState()
	const {user} =  useParams()
	const [isError, setIsError] = useState(false)

	useEffect(() => {
		const userDetail = async() => {
			setIsError(false)
			try {
				const result = await axios.get('http://localhost:8000/api/note/view/{user}')
				setData(result.data)
			}catch(error){
				setIsError(true)
			}
		}
		userDetail({user})

	}, [user])


	return(
		 <>
      <Flex>

      {isError ? (<Error/>) : (
			<Box maxW="sm" borderWidth="1px" rounded="lg" overflow="hidden">
				<Avatar size="2xl" name={data.first} />
				<Box>
          			{data.first}
        		</Box>
        		<Box>
          			{user.last}
        		</Box>        
        		<Box>
          			{data.display_name}
          		</Box>
			</Box>
			)}

      </Flex>
    </>

		)
}