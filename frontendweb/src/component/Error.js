import {
  Alert,
  AlertIcon,
  AlertTitle,
  AlertDescription,
  Flex,
  CloseButton,
} from "@chakra-ui/core";
import React from 'react';

export default function Error() {
  return(
        <Flex justify='center' >
          <Alert status="error">
  <AlertIcon />
  <AlertTitle mr={2}>Oops! An error occured</AlertTitle>
  <AlertDescription>Please refresh page or try again later</AlertDescription>
  <CloseButton position="absolute" right="8px" top="8px" />
</Alert>
        </Flex>
      );
}