import React from 'react'
import { Box, Flex } from '@chakra-ui/core'
import NoteDetail from './NoteDetail'

export default function Note({note}) {

	return(
		<Flex
      align='center'
      justify='flex-end'
      direction='column'
      bg='teal'
      width='300px'
      height='300px'
      borderRadius='40px'
      margin='16px'
      padding='16px'
    >

      <Box as='button' size='144px' bg='white' color='teal' textAlign='center' isTruncated>
        {note.title}
        <Box as='span'>
        	{note.display_name}
        </Box>
        <NoteDetail note={note} key={note.pk}/>      
      </Box>
      </Flex>

		)
}