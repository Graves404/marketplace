import React from 'react';
import { Image } from 'antd';
import  ImageData  from '../models/ImageData';

interface Props {
  image: ImageData;
}

const ImagesComponent: React.FC<Props> = ({ image }) => {
  return(
    <div className="w-full h-full object-cover">
        <Image key={image.id} src={image.url_photo} width={200} className='object-center'/>
    </div>
  )
};

export default ImagesComponent;
