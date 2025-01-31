import React from 'react';
import { Image, notification } from 'antd';
import  ImageData  from '../models/ImageData';

const ImagesComponent: React.FC<ImageData> = ({ image }) => {
  return(
    <>
      <Image.PreviewGroup preview={{
        onChange: (current, prev) => notification.error({message:`current index: ${current} prev index: ${prev}`,placement:"topRight"}),
      }}>
        <Image key={image.id} src={image.url_photo} width={200}/>
      </Image.PreviewGroup>
    </>
  )
};

export default ImagesComponent;
