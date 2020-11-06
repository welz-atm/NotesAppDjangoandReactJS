import React, {useState, useEffect, useRef} from 'react'
import axios from 'axios'
import {useParams} from 'react-router-dom'
import {
  AlertDialog,
  AlertDialogBody,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogContent,
  AlertDialogOverlay,
  IconButton,
  Button
} from "@chakra-ui/core";
import Error from './Error.js'


export default function DeleteUser() {
	const [isError, setIsError] = useState(false)
  const [isDelete, setIsDelete] = useState(false)
	const {user} = useParams()
	const [isOpen, setIsOpen] = useState();
  	const onClose = () => setIsOpen(false);
  	const cancelRef = useRef();

	useEffect(() => {
		const deleteUser = async() => {
			setIsError(false)
			try {
				axios.get('http://localhost:8000/api/user/delete/{user}')
        setIsDelete(true)
			}catch(error){
				setIsError(true)
			}
		}

		deleteUser({user})
	}, [user])

  if(isError){
    <Error/>
  }
	
	return(

		<>
      <IconButton
  			variantColor="teal"
  			aria-label="Delete User"
  			size="sm"
  			icon="delete"
		/>

      <AlertDialog
        isOpen={isOpen}
        leastDestructiveRef={cancelRef}
        onClose={onClose}
      >
        <AlertDialogOverlay />
        <AlertDialogContent>
          <AlertDialogHeader fontSize="lg" fontWeight="bold">
            Delete Note
          </AlertDialogHeader>

          <AlertDialogBody>
            Are you sure? You can't undo this action afterwards.
          </AlertDialogBody>

          <AlertDialogFooter>
            <Button ref={cancelRef} onClick={onClose}>
              Cancel
            </Button>
            <Button variantColor="red" onClick={isDelete} ml={3}>
              Delete
            </Button>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </>

		)
}