// var resizeTimeout;
// var xSheetData;
// var allowResize = true;
// var prevRowCount = -1; // Initialize a variable to keep track of the previous row count
// var sheet;
// var XsheetRows = -100;

// const options = {
//   row: {
//     len: 5000,
//   },
//   col: {
//     len: 500,
//   },
//   showToolbar: true,
//   view: {
//     height: () => $('#wrapper-s').outerHeight()+ 50,
//     width: () =>  $('#wrapper-s').outerWidth()+ 15,
//   },
// };

// function handleCellEdited(text, ri, ci) {
//   // Implement your logic to handle cell editing
//   console.log(`Cell edited: text = "${text}", row = ${ri}, column = ${ci}`);

//   // Send the result to the server
//   const data = {
//     text: text,
//     row: ri,
//     column: ci
//   };

//   makeAjaxRequest("POST", "/update", data, function(response) {
//     console.log(response);
//   });
// }

// function compare_sheets(xSheetData1, data) {
//   if (XsheetRows == -100){
//     XsheetRows = Object.keys(xSheetData1.rows).length;
//   }
//   const dataRows = Object.keys(data.rows);

//   lastrow = true;
//   console.log(dataRows.length);
//   console.log(XsheetRows.length);

//   if (dataRows.length-1 < XsheetRows) {
//     console.log('Row(s) deleted');
//     var idx;
//     var ridx;
//     for (idx of dataRows) {
//       if(idx != "len"){
//         ridx = idx
//         const xRowFirstCell = xSheetData1.rows[idx].cells['0'].text;
//         const dataRowFirstCell = data.rows[idx].cells['0'].text;
    
//         if (xRowFirstCell !== dataRowFirstCell) {
//           console.log(`Different first cell value at row ${idx}`);
//           const sendData = {
//             idx: idx,
//             row: data.rows[idx]
//           };
//           XsheetRows -=1 ;
//           makeAjaxRequest("POST", "/delete", sendData, function (response) {
//             xSheetData = response;
//           });
//           lastrow = false;
//         }
//       }
//     }
//     if (lastrow) {
//       idx = (parseInt(ridx, 10) + 1).toString(); // Convert back to string
//       console.log(idx);

//       console.log(xSheetData1.rows[idx]);

//       const sendData = {
//       idx: idx,
//       row: xSheetData1.rows[idx]
//       };      
//       XsheetRows -=1 ;
//       makeAjaxRequest("POST", "/delete", sendData, function (response) {
//         xSheetData = response;
//       });
//     }
//   }
//   else {
//     console.log('No rows deleted');
//   }
// }


// async function onload() {
//   await new Promise((resolve) => {
//     $('#loading-background').show();
//     setTimeout(resolve, 50);
//   });
  
//   await loadInitialData();
//   sheet = x_spreadsheet("#x-spreadsheet", options)
//   // Load generated data  
//   await sheet.loadData(xSheetData);
  
//   await sheet.change(data => {
//     compare_sheets(xSheetData[0], data);
//   });

//   // Edited on cell
//   sheet.on('cell-edited', (text, ri, ci) => {
//     handleCellEdited(text, ri, ci);
//   });

//   // data validation
//   await sheet.validate();
//   await new Promise((resolve) => {
//     dragResize();
//     setTimeout(resolve, 50);
//   });
//   $('#loading-background').hide();
// }


// async function toggleAll(drops) {
//   await Promise.all(
//     drops.map(drop => new Promise(resolve => {
//       drop.toggle();
//       setTimeout(resolve, 0);
//     }))
//   );
// }

// $(document).ready(function() {
//   const maxScroll = 4;
//   $('#wrapper-s').on('scroll', function() {
//     if ($(this).scrollLeft() > maxScroll) {
//       $(this).scrollLeft(maxScroll);
//     }
//   });
// });

// async function updateSpreadsheetSize() {
//   // Disable resizing and show loading screen
//   allowResize = false;
//   await new Promise((resolve) => {
//     $('#loading-background_s').show();
//     setTimeout(resolve, 100);
//   });
//   await $("#x-spreadsheet").empty();

//   // Update container size
//   sheet = x_spreadsheet("#x-spreadsheet", options)
//   await sheet.loadData(xSheetData) // load data


//   // data validation
//   await sheet.validate();

//   // Re-enable resizing and hide loading screen after a delay (e.g., 0 ms)
//   setTimeout(() => {
//     allowResize = true;
//     $('#loading-background_s').hide();
//   }, 1);
// }

// function dragResize(element){
//   var x = 0; var y = 0
//   interact('.draggable')
//   .resizable({
//     // resize from all edges and corners
//     edges: {right: true, bottom: true},
//     listeners: {
//       move(event) {
//         if (!allowResize) return;
//         var target = event.target;
//         var x = (parseFloat(target.getAttribute('data-x')) || 0);
//         var y = (parseFloat(target.getAttribute('data-y')) || 0);
      
//         // update the element's style
//         target.style.width = event.rect.width + 'px';
//         target.style.height = event.rect.height + 'px';
      
//         // translate when resizing from top or left edges
//         x += event.deltaRect.left;
//         y += event.deltaRect.top;
      
//         target.style.transform = 'translate(' + x + 'px,' + y + 'px)';
      
//         target.setAttribute('data-x', x);
//         target.setAttribute('data-y', y);

//         // Clear any existing timeout
//         if (resizeTimeout) {
//           clearTimeout(resizeTimeout);
//         }

//         // Set a new timeout to call updateSpreadsheetSize after 2 seconds
//         resizeTimeout = setTimeout(() => {
//           updateSpreadsheetSize();
//         }, 250);
//       }
//     },
//     inertia: true
//   })
//   .draggable({
//     modifiers: [
//       interact.modifiers.snap({
//         targets: [
//           interact.snappers.grid({ x: 50, y: 50 })
//         ],
//         range: Infinity,
//         relativePoints: [ { x: 10, y: 10 } ]
//       }),
//       interact.modifiers.restrict({
//         elementRect: { top: 0, left: 0, bottom: 1, right: 1 },
//         endOnly: true
//       })
//     ],
//     inertia: true
//   })
//   .on('dragmove', function (event) {
//     x += event.dx
//     y += event.dy
//     event.target.setAttribute('data-x', x)
//     event.target.setAttribute('data-y', y)
//     event.target.style.transform = 'translate(' + x + 'px, ' + y + 'px)'
//   })
// }

$("#logout").click(function(event) {
  // send an AJAX request to the server to check the login credentials
  makeAjaxRequest("GET", "/");
});

