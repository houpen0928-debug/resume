/* Store-only ZIP writer: packages local files without a server or credentials. */
window.journalZip = async function(entries) {
  const encoder = new TextEncoder();
  const locals = [], directory = [];
  let offset = 0;
  const crc32 = bytes => {
    let crc = 0xffffffff;
    for (const byte of bytes) {
      crc ^= byte;
      for (let bit = 0; bit < 8; bit++) crc = (crc >>> 1) ^ ((crc & 1) ? 0xedb88320 : 0);
    }
    return (crc ^ 0xffffffff) >>> 0;
  };
  for (const entry of entries) {
    const name = encoder.encode(entry.name);
    const bytes = typeof entry.data === 'string' ? encoder.encode(entry.data) : new Uint8Array(await entry.data.arrayBuffer());
    const crc = crc32(bytes);
    const header = new Uint8Array(30 + name.length), view = new DataView(header.buffer);
    view.setUint32(0,0x04034b50,true); view.setUint16(4,20,true); view.setUint16(6,0x800,true);
    view.setUint16(12,33,true); view.setUint32(14,crc,true); view.setUint32(18,bytes.length,true); view.setUint32(22,bytes.length,true); view.setUint16(26,name.length,true); header.set(name,30);
    const central = new Uint8Array(46 + name.length), cv = new DataView(central.buffer);
    cv.setUint32(0,0x02014b50,true); cv.setUint16(4,20,true); cv.setUint16(6,20,true); cv.setUint16(8,0x800,true); cv.setUint16(14,33,true);
    cv.setUint32(16,crc,true); cv.setUint32(20,bytes.length,true); cv.setUint32(24,bytes.length,true); cv.setUint16(28,name.length,true); cv.setUint32(42,offset,true); central.set(name,46);
    locals.push(header,bytes); directory.push(central); offset += header.length + bytes.length;
  }
  const end = new Uint8Array(22), ev = new DataView(end.buffer);
  ev.setUint32(0,0x06054b50,true); ev.setUint16(8,entries.length,true); ev.setUint16(10,entries.length,true);
  ev.setUint32(12,directory.reduce((sum,item)=>sum+item.length,0),true); ev.setUint32(16,offset,true);
  return new Blob([...locals,...directory,end],{type:'application/zip'});
};
