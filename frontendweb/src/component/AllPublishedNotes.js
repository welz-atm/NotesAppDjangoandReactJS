import React, {useState, useEffect} from 'react'
import { Flex } from '@chakra-ui/core'
import axios from 'axios'
import Error from './Error'
import Loading from './Loading'
import Note from './Note'


export default function AllPublishedNotes() {
	const [data, setData] = useState([])
	const [isError, setIsError] = useState(false)
	const [isLoading, setIsLoading] = useState(false)

	useEffect(() => {
		const allPublished = async() => {
			setIsError(false)
			setIsLoading(true)
			try {
				const result = await axios.get('http://localhost:8000/api/note/published_notes/')
				setData(result.data)
				console.log(result.data)
			}catch(error){
				setIsLoading(false)	
				setIsError(true)
			}		
		}
		allPublished()

	}, [])

	const noData = !data

	return(
		<>
    <Flex 
    	justify='center'
        align='center'
        flexWrap='wrap'
        flexDirection={noData ? 'column' : 'row'}
        margin='16px'
        padding='16px'>

        { isLoading && !isError ? (<Loading/>) : isError ? (<Error/>) : 
        	( data.map((note) =>(<Note key={note.pk} note={note}/>)) )
        } 
      
    </Flex>
    </>

		)
}