const dbName = "myDatabase";
const storeName = "xSheetData";

async function loadInitialData() {
  return new Promise((resolve, reject) => {
    const openRequest = indexedDB.open(dbName);

    openRequest.onupgradeneeded = (event) => {
      console.log('Database upgrade needed');

      const db = event.target.result;

      if (!db.objectStoreNames.contains(storeName)) {
        const objectStore = db.createObjectStore(storeName);
        console.log(`Object store "${storeName}" created`);
      }
    };

    openRequest.onsuccess = (event) => {
      console.log('Successfully connected to the database:', dbName);
      const db = event.target.result;
      const transaction = db.transaction(storeName, 'readonly');
      const objectStore = transaction.objectStore(storeName);
      const countRequest = objectStore.count();

      countRequest.onsuccess = (event) => {
        const count = event.target.result;
        console.log(`Object store "${storeName}" has ${count} value(s)`);

        if (count <= 0) {
          console.log('Loading initial data from API');
          makeAjaxRequest('GET', '/load_init', null, (response) => {
            console.log('Retrieved data from API:', response);
            xSheetData = response;

            const transaction = db.transaction(storeName, 'readwrite');
            const objectStore = transaction.objectStore(storeName);
            objectStore.add(response, 1);

            resolve(response);
          });

        } else {
          console.log('Loading initial data from IndexedDB');
          const getAllRequest = objectStore.getAll();

          getAllRequest.onsuccess = function() {
            console.log('Retrieved data from IndexedDB');
            xSheetData = getAllRequest.result[0];
            resolve(getAllRequest.result);
          };
        }
      };
    };
  });
}
  

function deleteDatabase(dbName) {
  return new Promise((resolve, reject) => {
    const deleteRequest = indexedDB.deleteDatabase(dbName);

    deleteRequest.onsuccess = () => {
      console.log(`Database "${dbName}" deleted successfully`);
      resolve();
    };

    deleteRequest.onerror = (event) => {
      console.error(`Error deleting database "${dbName}"`, event);
      reject(event);
    };

    deleteRequest.onblocked = () => {
      console.error(`Database "${dbName}" deletion blocked`);
      reject(new Error('Database deletion blocked'));
    };
  });
}


// deleteDatabase("myDatabase")
//   .then(() => {
//     console.log('Database deleted successfully');
//   })
//   .catch((error) => {
//     console.error('Error deleting database:', error);
//   });
