import React, {useState, useEffect} from 'react'
import { Flex, Text, Link } from '@chakra-ui/core'
import { Link as ReachLink } from "react-router-dom";
import axios from 'axios'
import Error from './Error.js'
import Loading from './Loading.js'


export default function MyUnPublishedNotes() {
	const [data, setData] = useState()
	const [isError, setIsError] = useState(false)
	const [isLoading, setIsLoading] = useState(false)

	useEffect(() => {
		const myUnPublishedNotes = async() => {
			setIsError(false)
			setIsLoading(true)
			try {
				const result = await axios.get('http://localhost:8000/api/note/myunpublished_notes/')
				setData(result.data)
			}catch(error){
				setIsError(true)
			}
			setIsLoading(false)			
		}
		myUnPublishedNotes()

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
      		data.map((note, index) => 
      			<Link as={ReachLink} to='/noteDetail'>
      				<Text>{note.title} {note.display_name}</Text>
      			</Link>))}
			
		</Flex>

		)
}