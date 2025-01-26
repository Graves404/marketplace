import React from 'react';
import { Image } from 'antd';
import  ImageData  from '../models/ImageData';

const ImagesComponent: React.FC<ImageData> = ({ image }) => {
  return(
    <>
      <Image.PreviewGroup preview={{
        onChange: (current, prev) => console.log(`current index: ${current}, prev index: ${prev}`),
      }}>
        <Image key={image.id} src={image.url_photo} width={200}/>
      </Image.PreviewGroup>
    </>
  )
};

export default ImagesComponent;