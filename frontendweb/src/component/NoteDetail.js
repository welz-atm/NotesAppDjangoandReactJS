import React, {useState, useEffect, useRef } from 'react'
import { Button,
         IconButton,
         Modal,
         ModalFooter,
         ModalContent,
         ModalHeader,
         ModalCloseButton,
         ModalOverlay,
         ModalBody,
         useDisclosure } from '@chakra-ui/core';
import axios from 'axios'
import {useParams} from 'react-router-dom'
import Error from './Error'


export default function NoteDetail() {
	const [data, setData] = useState()
	const {note} = useParams()
	const [isError, setIsError] = useState(false)
	const {isOpen, onOpen, onClose} = useDisclosure();
  const btnRef = useRef();

	useEffect(() => {
		const noteDetail = async() => {
			setIsError(false)
			try {
				const result = await axios.get('http://localhost:8000/api/note/view/', {note})
				setData(result.data)
			}catch(error){
				setIsError(true)
			}
		}
		noteDetail(note)

	}, [note])

	if(isError)return <Error/>


	return(
		 <>
      <IconButton
          variantColor="teal"
          aria-label="View Note"
          size="sm"
          icon="view"
          onClick={ onOpen }
        />

      <Modal closeOnOverlayClick={false} isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>{ data.title }</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            { data.description }
          </ModalBody>

          <ModalFooter>
            <Button onClick={onClose} ref={btnRef}>Close</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>

		)
}