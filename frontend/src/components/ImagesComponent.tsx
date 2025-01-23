import React from 'react';
import { Image } from 'antd';
import { ImageData } from '../models/ImageData';

const ImagesComponent: React.FC<ImageData> = ({ image }) => {
  return(
    <>
      <Image
        width={200}
        src={image.url_photo}
      />
    </>
  )
};

export default ImagesComponent;