import React from 'react';
import { Image } from 'antd';

const Images: React.FC = () => (
  <Image.PreviewGroup
    preview={{
      onChange: (current, prev) => console.log(`current index: ${current}, prev index: ${prev}`),
    }}>
    
    <Image width={200} src="https://firebasestorage.googleapis.com/v0/b/market-479da.firebasestorage.app/o/images%2FElsie's%20Library%20_%20Fall%202020%20Reading%20List.jpg?alt=media&token=9f9cd17d-d641-4a50-a85b-10cd9dc90ee4" />
    <Image
      width={200}
      src="https://firebasestorage.googleapis.com/v0/b/market-479da.firebasestorage.app/o/images%2FElsie's%20Library%20_%20Fall%202020%20Reading%20List.jpg?alt=media&token=9f9cd17d-d641-4a50-a85b-10cd9dc90ee4"
    />
  </Image.PreviewGroup>
);

export default Images;
