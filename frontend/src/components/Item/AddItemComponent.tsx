import React, { useState } from 'react';
import { PlusOutlined } from '@ant-design/icons';
import { Form, Input, Upload, notification, Button } from 'antd';
import type { UploadFile } from 'antd/es/upload/interface';
import Cookies from 'js-cookie';
  

const normFile = (e: {fileList: UploadFile[]} | UploadFile[]) => {
    if (Array.isArray(e)) {
        return e;
    }
    return e?.fileList;
};

type FormValues = {
    title: string;
    description: string;
    price: string;
    city: string;
    images?: UploadFile[];
}
  

const AddItemComponent: React.FC<{ onSuccess: () => void }> = ({ onSuccess }) => {

    const [loading, setLoading] = useState(false);

    const [fileList, setFileList] = useState<UploadFile[]>([]);

    const handleFileChange = ({ fileList }: {fileList: UploadFile[]}) => {
        setFileList(fileList);
    };

    const onFinish = async (value : FormValues) => {
        setLoading(true);
        try {
            const token = Cookies.get("mne_market_accesses_token");
            
            const formData = new FormData();

            formData.append('title', value.title);
            formData.append('description', value.description);
            formData.append('price', value.price);
            formData.append('city', value.city);

            fileList.forEach((file) => {
                formData.append('files', file.originFileObj as Blob);
            });

            const response = await fetch('http://127.0.0.1:8000/items/add_item', {
                method : "POST",
                headers : {
                    'Authorization': `Bearer ${token}`
                },
                body : formData
            });

            if(response.ok) {
                notification.success({ message: "Item added successfully!", placement:"topRight"});
                onSuccess();
                setTimeout(() => {
                    window.location.reload();
                }, 1000)
            } else {
                notification.error({ message : "Failed to add item", placement : "topRight" });
            }

        } catch(error) {
            notification.error({message:`Error ${error}`, placement:"topRight"});
        } finally {
            setLoading(false);
        }
    }

    return (
        <div>
            <Form onFinish={onFinish} labelCol={{ span: 4 }} wrapperCol={{ span: 14 }} layout="horizontal" style={{ maxWidth: 600 }}>
                <Form.Item label="Title" name="title">
                    <Input />
                </Form.Item>
                <Form.Item label="Decription" name="description">
                    <Input />
                </Form.Item>
                <Form.Item label="Price" name="price">
                    <Input />
                </Form.Item>
                <Form.Item label="City" name="city">
                    <Input />
                </Form.Item>
                <Form.Item label="Upload" name="images" valuePropName="fileList" getValueFromEvent={normFile}>
                    <Upload multiple listType="picture-card" fileList={fileList} beforeUpload={() => false} onChange={handleFileChange}>
                        <button style={{ border: 0, background: 'none' }} type="button">
                            <PlusOutlined />
                            <div style={{ marginTop: 8 }}>Upload</div>
                        </button>
                    </Upload>
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit" loading={loading}>Add</Button>
                </Form.Item>
            </Form>
        </div>
    )
}

export default AddItemComponent;