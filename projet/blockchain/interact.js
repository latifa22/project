// This will return an array of available Ethereum addresses (accounts)
let accounts = await web3.eth.getAccounts();
const interact = async () => {
    // Get an instance of the deployed contract
    let instance = await IdentityContract.deployed();
  
    // Use one of the available accounts as the sender
    let senderAddress = accounts[0];
  
    // Call contract functions
    let result = await instance.setIdentity("ahmedhmida", { from: senderAddress });
    console.log(result);
  
    let identity = await instance.getIdentity({ from: senderAddress });
    console.log(identity);
  };
  
  interact();
  